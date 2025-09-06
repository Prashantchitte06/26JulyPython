#Ex2: Single Level Inheritance

class WhatsAppV1:
    def chat(self):
        print("chat feature")

class WhatsAppV2(WhatsAppV1):
    def audioCalling(self):
        print("Audio Calling feature")

    # def chat(self):
    #     print("chat feature")

class WhatsAppV3(WhatsAppV2):
    def videoCalling(self):
        print("video Calling feature")

    # def audioCalling(self):
    #     print("Audio Calling feature")

    # def chat(self):
    #     print("chat feature")

w3=WhatsAppV3()
w3.chat()
w3.audioCalling()
w3.videoCalling()




