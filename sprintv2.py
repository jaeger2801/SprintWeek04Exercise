{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "aced9aea",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3c673828",
   "metadata": {},
   "outputs": [],
   "source": [
    "datosUsuarios = {'Nombre': ['Carlos', 'Juliana', 'Camila'],\n",
    "         'Edad': [18, 32, 25],\n",
    "         'Estatura en CM': ['182', '153', '160']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "12b10d7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(datosUsuarios)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "10893311",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('sprintv2.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "28ade65b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "0   Carlos    18            182\n",
       "1  Juliana    32            153\n",
       "2   Camila    25            160"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6ef9aae5",
   "metadata": {},
   "outputs": [],
   "source": [
    "Es = df.sort_values(by= 'Estatura en CM', ascending=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5146c2a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "1  Juliana    32            153\n",
       "2   Camila    25            160\n",
       "0   Carlos    18            182"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Es"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7918ad21",
   "metadata": {},
   "outputs": [],
   "source": [
    "EsDesc = df.sort_values(by= 'Estatura en CM', ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0d1e8b8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "0   Carlos    18            182\n",
       "2   Camila    25            160\n",
       "1  Juliana    32            153"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "EsDesc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "33082f31",
   "metadata": {},
   "outputs": [],
   "source": [
    "Nom_AtoZ = df.sort_values(by= 'Nombre', ascending=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "68514275",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "2   Camila    25            160\n",
       "0   Carlos    18            182\n",
       "1  Juliana    32            153"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Nom_AtoZ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "614c0bee",
   "metadata": {},
   "outputs": [],
   "source": [
    "Nom_ZtoA = df.sort_values(by= 'Nombre', ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d382d01e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "1  Juliana    32            153\n",
       "0   Carlos    18            182\n",
       "2   Camila    25            160"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Nom_ZtoA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "760b8b06",
   "metadata": {},
   "outputs": [],
   "source": [
    "NameAgeHeight = df.sort_values(by= ['Nombre','Estatura en CM', 'Edad'], ascending=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e4cc1e21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nombre</th>\n",
       "      <th>Edad</th>\n",
       "      <th>Estatura en CM</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Camila</td>\n",
       "      <td>25</td>\n",
       "      <td>160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Carlos</td>\n",
       "      <td>18</td>\n",
       "      <td>182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Juliana</td>\n",
       "      <td>32</td>\n",
       "      <td>153</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nombre  Edad Estatura en CM\n",
       "2   Camila    25            160\n",
       "0   Carlos    18            182\n",
       "1  Juliana    32            153"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "NameAgeHeight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d536abbb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
