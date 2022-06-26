from db_config import Message


def create_message():
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

    Message.create(user="Tom", content="Hello Bob!")


def display_all_message():
    for msg in Message.select():  # sselectは複数の情報を取ってくる
        print(msg.id, msg.user, msg.content, msg.pub_date)


def find_message(id):
    msg = Message.get(Message.id == id)  # getは一つの値を取ってくる
    print(msg.id, msg.user, msg.content, msg.pub_date)


def main():
    # create_message()
    display_all_message()

    # id = 1
    # find_message(id)

    # id = 1
    # whereは複数の後にしか使えないため、getではなくselectを使う
    # delete_user()

    id = 2
    msg = Message.select().where(Message.id == id).get()
    msg.user = "Tom Ford"
    msg.save()


def delete_user():
    msg = Message.select().where(Message.id == id).get()
    msg.delete_instance()




if __name__ == "__main__":
    main()