{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Breast  Cancer Classification .ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP6UlLJBPGH93s5o6hX3nLV",
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
        "<a href=\"https://colab.research.google.com/github/Shoeb-Shaon/Breast-Cancer-Classification/blob/main/Breast_Cancer_Classification_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Loading and preprocesing"
      ],
      "metadata": {
        "id": "UNoexj8UqPPs"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importing libraries"
      ],
      "metadata": {
        "id": "a98c-mhD-cY2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import os\n",
        "import math\n",
        "import shutil\n",
        "import glob\n",
        "from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense, BatchNormalization, GlobalAvgPool2D\n",
        "from keras.models import Sequential\n",
        "from keras.preprocessing.image import ImageDataGenerator\n",
        "import keras"
      ],
      "metadata": {
        "id": "-1g-SI3ZpcIF"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "root_dir=\"/content/drive/MyDrive/Thesis resources/Datasets/dataset'/Mini_DDSM_Upload\"\n",
        "number_of_images={}\n",
        "for dir in os.listdir(root_dir):\n",
        "  number_of_images[dir]=len(os.listdir(os.path.join(root_dir,dir)))"
      ],
      "metadata": {
        "id": "CVrG5qFB6Ye-"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Creating Traning Folder"
      ],
      "metadata": {
        "id": "VnOL3Nns-S1G"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "def dataFolder(p,split):\n",
        "  if not os.path.exists(\"/content/drive/MyDrive/\"+p):\n",
        "    os.mkdir(\"/content/drive/MyDrive/\"+p)\n",
        "    for dir in os.listdir(root_dir):\n",
        "      os.makedirs(\"/content/drive/MyDrive/\"+p+\"/\"+dir)\n",
        "      for img in np.random.choice(a=os.listdir(os.path.join(root_dir,dir)),size=(math.floor(split*number_of_images[dir])-5),replace=False):\n",
        "        O=os.path.join(root_dir,dir,img)\n",
        "        D=os.path.join(\"/content/drive/MyDrive/\"+p,dir)\n",
        "        shutil.copy(O,D)\n",
        "        os.remove(O)\n",
        "  else:\n",
        "    print(f\"{p} Folder exist\")"
      ],
      "metadata": {
        "id": "wen9yrBIvd2J"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dataFolder(\"thesis_train\",0.7)\n",
        "dataFolder(\"thesis_test\",0.15)\n",
        "dataFolder(\"thesis_val\",0.15)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yYlsMNJv-pKW",
        "outputId": "e9201e89-e6a5-4315-c367-639369d2172e"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "thesis_train Folder exist\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "root_dir=\"/content/drive/MyDrive/Thesis resources/Datasets/dataset'/Mini_DDSM_Upload\"\n",
        "number_of_images={}\n",
        "for dir in os.listdir(root_dir):\n",
        "  number_of_images[dir]=len(os.listdir(os.path.join(root_dir,dir)))\n",
        "number_of_images.items()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_5kuVfMj-p3Q",
        "outputId": "ca574678-1ad8-49b7-d9cc-bbfa58d8ddfb"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "dict_items([('Normal', 16), ('Cancer', 16), ('Benign', 16)])"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Basic CNN model"
      ],
      "metadata": {
        "id": "0h7PzQL-ABls"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#CNN Model\n",
        "model= Sequential()\n",
        "model.add(Conv2D(filters=16,kernel_size=(3,3), activation= 'relu', input_shape=(224,224,3)))\n",
        "\n",
        "model.add(Conv2D(filters=32,kernel_size=(3,3), activation= 'relu'))\n",
        "model.add(MaxPool2D(pool_size=(2,2)))\n",
        "\n",
        "model.add(Conv2D(filters=64,kernel_size=(3,3), activation= 'relu'))\n",
        "model.add(MaxPool2D(pool_size=(2,2)))\n",
        "\n",
        "model.add(Conv2D(filters=128,kernel_size=(3,3), activation= 'relu'))\n",
        "model.add(MaxPool2D(pool_size=(2,2)))\n",
        "\n",
        "model.add(Dropout(rate=0.25))\n",
        "\n",
        "model.add(Flatten())\n",
        "model.add(Dense(units=64, activation= 'relu'))\n",
        "model.add(Dense(units=1, activation='sigmoid'))\n",
        "model.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2klRHJphAHW-",
        "outputId": "181d1039-5795-43dd-8403-c98b047e9e8d"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " conv2d (Conv2D)             (None, 222, 222, 16)      448       \n",
            "                                                                 \n",
            " conv2d_1 (Conv2D)           (None, 220, 220, 32)      4640      \n",
            "                                                                 \n",
            " max_pooling2d (MaxPooling2D  (None, 110, 110, 32)     0         \n",
            " )                                                               \n",
            "                                                                 \n",
            " conv2d_2 (Conv2D)           (None, 108, 108, 64)      18496     \n",
            "                                                                 \n",
            " max_pooling2d_1 (MaxPooling  (None, 54, 54, 64)       0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " conv2d_3 (Conv2D)           (None, 52, 52, 128)       73856     \n",
            "                                                                 \n",
            " max_pooling2d_2 (MaxPooling  (None, 26, 26, 128)      0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " dropout (Dropout)           (None, 26, 26, 128)       0         \n",
            "                                                                 \n",
            " flatten (Flatten)           (None, 86528)             0         \n",
            "                                                                 \n",
            " dense (Dense)               (None, 64)                5537856   \n",
            "                                                                 \n",
            " dense_1 (Dense)             (None, 1)                 65        \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 5,635,361\n",
            "Trainable params: 5,635,361\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "xp8-tOT__-oN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(optimizer='adam',loss=keras.losses.binary_crossentropy, metrics=['accuracy'])"
      ],
      "metadata": {
        "id": "llAbzdkjAK2U"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def preprocessingImages1(path):\n",
        "  image_data=ImageDataGenerator(zoom_range=0.2,shear_range=0.2, rescale=1/255, horizontal_flip=True)\n",
        "  image= image_data.flow_from_directory(directory=path, target_size=(224,224), batch_size=32, class_mode= 'binary')\n",
        "\n",
        "  return image "
      ],
      "metadata": {
        "id": "3Rvds5boAOvu"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "path=\"/content/drive/MyDrive/thesis_train\"\n",
        "train_data= preprocessingImages1(path)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bFY9pLFPCNDu",
        "outputId": "3a30a783-7b9f-4b37-a6cb-7bd12ae38885"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 6772 images belonging to 3 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def preprocessingImages2(path):\n",
        "  image_data=ImageDataGenerator(rescale=1/255)\n",
        "  image= image_data.flow_from_directory(directory=path, target_size=(224,224), batch_size=32, class_mode= 'binary')\n",
        "\n",
        "  return image "
      ],
      "metadata": {
        "id": "57FWU1iyDjLi"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "path=\"/content/drive/MyDrive/thesis_test\"\n",
        "test_data= preprocessingImages2(path)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5z5-3bXgDkIT",
        "outputId": "4c84dde9-8295-405b-956f-69e608ae7c9e"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 1439 images belonging to 3 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "path=\"/content/drive/MyDrive/thesis_val\"\n",
        "val_data= preprocessingImages2(path)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "btQhh1C5D0m8",
        "outputId": "472b2283-592c-4d80-df50-321e643c8645"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 1439 images belonging to 3 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# early stopping and model check point\n",
        "from keras.callbacks import ModelCheckpoint, EarlyStopping\n",
        "\n",
        "#Early stopping\n",
        "es=EarlyStopping (monitor=\"val_accuracy\",min_delta=0.01, patience=6, verbose=1, mode='auto')\n",
        "\n",
        "#model check point\n",
        "mc= ModelCheckpoint(monitor=\"val_accuracy\",filepath=\"/content/drive/MyDrive/Thesis work/bmodel.h5\",verbose=1, save_best_only=True, mode='auto')\n",
        "cd=[es,mc]\n"
      ],
      "metadata": {
        "id": "PA_gnZdQD4zZ"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model traning"
      ],
      "metadata": {
        "id": "oYlYUf-LD61S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# model Training\n",
        "hs=model.fit_generator(generator=train_data, steps_per_epoch=8, epochs=60, verbose=1, validation_data=val_data, validation_steps=16, callbacks=cd )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lOtzTzKbD6XW",
        "outputId": "37e0f23b-e3fd-4300-ca59-f88373db075c"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:2: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.\n",
            "  \n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 0.8059 - accuracy: 0.4023\n",
            "Epoch 1: val_accuracy improved from -inf to 0.38477, saving model to /content/drive/MyDrive/Thesis work/bmodel.h5\n",
            "8/8 [==============================] - 41s 5s/step - loss: 0.8059 - accuracy: 0.4023 - val_loss: 0.1242 - val_accuracy: 0.3848\n",
            "Epoch 2/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -0.3600 - accuracy: 0.3555\n",
            "Epoch 2: val_accuracy did not improve from 0.38477\n",
            "8/8 [==============================] - 40s 5s/step - loss: -0.3600 - accuracy: 0.3555 - val_loss: 0.5067 - val_accuracy: 0.3691\n",
            "Epoch 3/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 0.0090 - accuracy: 0.3867 \n",
            "Epoch 3: val_accuracy did not improve from 0.38477\n",
            "8/8 [==============================] - 40s 5s/step - loss: 0.0090 - accuracy: 0.3867 - val_loss: 0.1398 - val_accuracy: 0.3535\n",
            "Epoch 4/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 0.0943 - accuracy: 0.3867\n",
            "Epoch 4: val_accuracy did not improve from 0.38477\n",
            "8/8 [==============================] - 40s 5s/step - loss: 0.0943 - accuracy: 0.3867 - val_loss: -0.3614 - val_accuracy: 0.3633\n",
            "Epoch 5/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -1.9192 - accuracy: 0.3945\n",
            "Epoch 5: val_accuracy improved from 0.38477 to 0.38672, saving model to /content/drive/MyDrive/Thesis work/bmodel.h5\n",
            "8/8 [==============================] - 41s 5s/step - loss: -1.9192 - accuracy: 0.3945 - val_loss: 1.8054 - val_accuracy: 0.3867\n",
            "Epoch 6/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -54.0464 - accuracy: 0.3672\n",
            "Epoch 6: val_accuracy did not improve from 0.38672\n",
            "8/8 [==============================] - 40s 5s/step - loss: -54.0464 - accuracy: 0.3672 - val_loss: -24.1805 - val_accuracy: 0.3828\n",
            "Epoch 7/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 210.8732 - accuracy: 0.3984\n",
            "Epoch 7: val_accuracy improved from 0.38672 to 0.39648, saving model to /content/drive/MyDrive/Thesis work/bmodel.h5\n",
            "8/8 [==============================] - 40s 5s/step - loss: 210.8732 - accuracy: 0.3984 - val_loss: 29.1298 - val_accuracy: 0.3965\n",
            "Epoch 8/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 16.9798 - accuracy: 0.4023\n",
            "Epoch 8: val_accuracy improved from 0.39648 to 0.41211, saving model to /content/drive/MyDrive/Thesis work/bmodel.h5\n",
            "8/8 [==============================] - 41s 5s/step - loss: 16.9798 - accuracy: 0.4023 - val_loss: -4.7593 - val_accuracy: 0.4121\n",
            "Epoch 9/60\n",
            "8/8 [==============================] - ETA: 0s - loss: 1.1292 - accuracy: 0.3516\n",
            "Epoch 9: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: 1.1292 - accuracy: 0.3516 - val_loss: -37.8013 - val_accuracy: 0.3633\n",
            "Epoch 10/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -32.3615 - accuracy: 0.3555\n",
            "Epoch 10: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: -32.3615 - accuracy: 0.3555 - val_loss: -36.6301 - val_accuracy: 0.3457\n",
            "Epoch 11/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -43.3689 - accuracy: 0.3359\n",
            "Epoch 11: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: -43.3689 - accuracy: 0.3359 - val_loss: -55.4516 - val_accuracy: 0.3809\n",
            "Epoch 12/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -125.4783 - accuracy: 0.3477\n",
            "Epoch 12: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: -125.4783 - accuracy: 0.3477 - val_loss: -25.7330 - val_accuracy: 0.3770\n",
            "Epoch 13/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -155.8986 - accuracy: 0.3711\n",
            "Epoch 13: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: -155.8986 - accuracy: 0.3711 - val_loss: 2.8352 - val_accuracy: 0.3711\n",
            "Epoch 14/60\n",
            "8/8 [==============================] - ETA: 0s - loss: -30.0338 - accuracy: 0.4062\n",
            "Epoch 14: val_accuracy did not improve from 0.41211\n",
            "8/8 [==============================] - 40s 5s/step - loss: -30.0338 - accuracy: 0.4062 - val_loss: 8.9550 - val_accuracy: 0.3828\n",
            "Epoch 14: early stopping\n"
          ]
        }
      ]
    }
  ]
}