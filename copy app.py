import tkinter as tk
import customtkinter as ck

import pandas as pd
import numpy as np
import pickle
import mediapipe as mp
import cv2
from PIL import Image, ImageTk
from landmarks import landmarks

window = tk.Tk()
window.geometry("480x700")
window.title("Fajar uji coba")
ck.set_appearance_mode("dark")

classLabel = ck.CTkLabel(window, height=40, width = 120, text_font=("Arial"))