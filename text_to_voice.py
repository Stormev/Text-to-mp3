import playsound
import gtts


def text_to_voice(file_path, file_save, play_sound=False):
    with open(file_path, "r", encoding="utf-8") as file_read:
        sound = gtts.gTTS(file_read.read(), lang="ru")
        sound.save(file_save)
        if play_sound:
            playsound.playsound("sound.mp3")
