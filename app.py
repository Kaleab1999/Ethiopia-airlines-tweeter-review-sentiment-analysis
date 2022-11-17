{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNiNAk/glFXvATg63A+jQ1K",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kaleab1999/Ethiopia-airlines-tweeter-review-sentiment-analysis/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "xTdMd4RYxbtb"
      },
      "outputs": [],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install transformers"
      ],
      "metadata": {
        "id": "JoxL7fOfxm-e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "from transformers import BertTokenizer, BertForSequenceClassification\n",
        "import torch\n",
        "\n",
        "#@st.cache(allow_output_mutation=True)\n",
        "\n",
        "tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')\n",
        "model = BertForSequenceClassification.from_pretrained(\"Kaleab1999/ethiopian-airlines\")\n",
        "\n",
        "\n",
        "user_input = st.text_area('Enter Text to Analyze')\n",
        "button = st.button(\"Analyze\")\n",
        "\n",
        "d = {\n",
        "    \n",
        "  1:'Neutral',\n",
        "  0:'Negative',\n",
        "  2:'positive'\n",
        "}\n",
        "\n",
        "if user_input and button :\n",
        "    test_sample = tokenizer([user_input], padding=True, truncation=True, max_length=512,return_tensors='pt')\n",
        "    # test_sample\n",
        "    output = model(**test_sample)\n",
        "    st.write(\"Logits: \",output.logits)\n",
        "    y_pred = np.argmax(output.logits.detach().numpy(),axis=1)\n",
        "    st.write(\"Prediction: \",d[y_pred[0]])"
      ],
      "metadata": {
        "id": "1VUUq5Ppxeik"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "0lEK9mtlxe_1"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}