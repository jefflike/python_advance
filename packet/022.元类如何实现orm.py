'''
__title__ = '002.元类如何实现orm.py'
__author__ = 'Jeffd'
__time__ = '4/23/18 7:28 PM'
'''
'''
    tips: 自定义一个简易orm
'''


class Field:
    pass


class CharField(Field):
    def __init__(self, db_column=None, max_lenth=None):
        self._value = None
        self.db_column = db_column

        if max_lenth is None:
            raise ValueError('请输入最大值')

        self.max_lenth = max_lenth

        if isinstance(max_lenth, int):
            if max_lenth < 0:
                raise ValueError('请输入正整数')
            self._value = max_lenth
        else:
            raise ValueError('请输入int类型')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        '''

        :param instance, 是user的对象<__main__.User object at 0x7f6390b50f28>:
        :param value:
        :return:
        '''
        if isinstance(value, str):
            if len(value) > self.max_lenth:
                raise ValueError('超出字符限制')
            self._value = value

        else:
            raise ValueError('请输入str类型')


class InterField(Field):

    def __init__(self, min_value, max_value, db_column=None):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        if isinstance(min_value, int):
            if min_value < 0:
                raise ValueError('请输入正整数')
            self._value = min_value
        else:
            raise ValueError('请输入int类型')

        if isinstance(max_value, int):
            if max_value < 0:
                raise ValueError('请输入正整数')
            self._value = max_value

        else:
            raise ValueError('请输入int类型')

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError('请输入正确的年龄区间')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        '''

        :param instance, 是user的对象<__main__.User object at 0x7f6390b50f28>:
        :param value:
        :return:
        '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('请输入正整数')
            if value < self.min_value or value > self.max_value:
                raise ValueError('请输入正确范围内数字')
            self._value = value

        else:
            raise ValueError('请输入int类型')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
            _meta['db_table'] = db_table
            attrs['_meta'] = _meta
            attrs['fields'] = fields
            del attrs['Meta']
            return super().__new__(cls, name, bases, attrs, *args, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))

        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta['db_table'],
                  fields=','.join(fields), values=','.join(values)
                                                )
        print(sql)


class User(BaseModel):
    name = CharField(db_column='name', max_lenth=5)
    age = InterField(db_column='age', min_value=0, max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == "__main__":
    user = User(name='jeffd', age=25)
    # user.name = 'jeffd'
    # user.age = 25
    user.save()