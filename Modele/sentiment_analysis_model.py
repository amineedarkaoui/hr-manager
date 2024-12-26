# importing librairies :
from transformers import pipeline
import torch
import streamlit as st


def modele(texte_to_analyse):
    classifier = pipeline("sentiment-analysis")
    res=classifier(texte_to_analyse)
    return res
