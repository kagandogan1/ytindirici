import streamlit as st
import pytube

url=st.text_input("İndireceğiniz Video'nun URL Adresini Yapıştırın")

if len(url)>0:

    sonuc=pytube.YouTube(url).streams.first().download()

    with open(sonuc, "rb") as file:
        btn = st.download_button(
                label="Video Olarak İndir",
                data=file,
                file_name="video.mp4",
                mime="video/mp4"
            )
        print("Video Başarıyla İndirildi")
    sonuc1=pytube.YouTube(url).streams.first().download()
    with open(sonuc1, "rb") as file:
        btn = st.download_button(
            label="Ses Olarak İndir",
            data=file,
            file_name="müzik.mp3",
            mime="audio/mp3"
        )
        print("Ses Başarıyla İndirildi")