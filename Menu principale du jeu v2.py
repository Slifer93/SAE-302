import tkinter as tk
from tkinter import messagebox
import pygame
import random

class BlindtestGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Blindtest Musical")
        self.master.geometry("500x400")

        pygame.mixer.init()

        self.genres = {
            "RAP FR": [...],  # Liste de chansons RAP FR
            "RAP US": [...],  # Liste de chansons RAP US
            "Latino": [...],  # Liste de chansons Latino
            "Bouyon": [...],  # Liste de chansons Bouyon
            "Variété FR": [...],  # Liste de chansons Variété FR
        }

        self.difficulties = {
            "Novice": 10,
            "Intermédiaire": 5,
            "Extrême": 3
        }

        self.selected_genre = None
        self.selected_difficulty = None
        self.current_playlist = []
        self.current_song_index = 0
        self.score = 0

        self.show_genre_selection()

    def show_genre_selection(self):
        self.clear_window()
        tk.Label(self.master, text="Choisissez un genre musical :", font=("Arial", 18)).pack(pady=20)

        for genre in self.genres.keys():
            tk.Button(self.master, text=genre, command=lambda g=genre: self.select_genre(g)).pack(pady=5)

    def select_genre(self, genre):
        self.selected_genre = genre
        self.show_difficulty_selection()

    def show_difficulty_selection(self):
        self.clear_window()
        tk.Label(self.master, text="Choisissez une difficulté :", font=("Arial", 18)).pack(pady=20)

        for difficulty in self.difficulties.keys():
            tk.Button(self.master, text=difficulty, command=lambda d=difficulty: self.select_difficulty(d)).pack(pady=5)

    def select_difficulty(self, difficulty):
        self.selected_difficulty = difficulty
        self.prepare_game()
        self.show_game_interface()

    def prepare_game(self):
        all_songs = self.genres[self.selected_genre]
        num_songs = self.difficulties[self.selected_difficulty]
        self.current_playlist = random.sample(all_songs, min(num_songs, len(all_songs)))
        self.current_song_index = 0
        self.score = 0

    def show_game_interface(self):
        self.clear_window()
        tk.Label(self.master, text=f"Genre: {self.selected_genre} - Difficulté: {self.selected_difficulty}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.master, text=f"Chanson {self.current_song_index + 1}/{len(self.current_playlist)}", font=("Arial", 12)).pack()

        self.play_button = tk.Button(self.master, text="Jouer l'extrait", command=self.play_music)
        self.play_button.pack(pady=10)

        self.answer_entry = tk.Entry(self.master, width=50)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Valider", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self.master, text=f"Score : {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=20)

    def play_music(self):
        if self.current_song_index < len(self.current_playlist):
            pygame.mixer.music.load(self.current_playlist[self.current_song_index]["file"])
            pygame.mixer.music.play()

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = self.current_playlist[self.current_song_index]["title"].lower()
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Bonne réponse!")
        else:
            messagebox.showinfo("Incorrect", f"La bonne réponse était : {correct_answer}")

        self.current_song_index += 1
        if self.current_song_index < len(self.current_playlist):
            self.update_game_interface()
        else:
            self.show_final_score()

    def update_game_interface(self):
        self.score_label.config(text=f"Score : {self.score}")
        self.master.title(f"Chanson {self.current_song_index + 1}/{len(self.current_playlist)}")
        self.answer_entry.delete(0, tk.END)

    def show_final_score(self):
        self.clear_window()
        tk.Label(self.master, text="Fin du jeu!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.master, text=f"Votre score final : {self.score}/{len(self.current_playlist)}", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.master, text="Rejouer", command=self.show_genre_selection).pack(pady=10)

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = BlindtestGame(root)
    root.mainloop()