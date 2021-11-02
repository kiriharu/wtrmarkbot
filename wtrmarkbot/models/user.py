from tortoise import fields, Model


class User(Model):
    telegram_id = fields.IntField(pk=True)
    position = fields.IntField(default=0)
    color = fields.CharField(max_length=255, default="Белый")
    opacity = fields.IntField(default=128)
    font = fields.CharField(max_length=255, default="Lobster")
    fontsize = fields.CharField(max_length=255, default=40)
    text = fields.CharField(max_length=255, default="Sample text...")
