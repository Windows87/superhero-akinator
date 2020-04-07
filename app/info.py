features = ['intelligence', 'strength', 'power', 'combat', 'speed', 'gender', 'is_tall', 'is_short', 'is_weight', 'is_light', 'is_bald', 'eye_color', 'publisher', 'place_of_birth']

questions = {
  'intelligence': 'O quão inteligente esse personagem é?',
  'strength': 'O quão forte esse personagem é?',
  'power': 'O quão poderoso esse personagem é?',
  'combat': 'O quão bom em artes marciais esse personagem é?',
  'speed': 'O quão rápido esse personagem é?',

  'gender': 'Esse personagem é homem?',
  'is_tall': 'Esse personagem é alto?',
  'is_short': 'Esse personagem é baixo?',
  'is_weight': 'Esse personagem é pesado?',
  'is_light': 'Esse personagem é leve?',
  'is_bald': 'Esse personagem é careca?',

  'eye_color': 'A cor do olho do personagem é ',
  'publisher': 'A Editora dele é a ',
  'place_of_birth': 'Ele nasceu em '
}

answers = {
  'intelligence': [{ 'title': 'Alta', 'value': 2 }, { 'title': 'Média', 'value': 1 }, { 'title': 'Baixa', 'value': 0 }],
  'strength': [{ 'title': 'Alta', 'value': 2 }, { 'title': 'Média', 'value': 1 }, { 'title': 'Baixa', 'value': 0 }],
  'power': [{ 'title': 'Alta', 'value': 2 }, { 'title': 'Média', 'value': 1 }, { 'title': 'Baixa', 'value': 0 }],
  'combat': [{ 'title': 'Alta', 'value': 2 }, { 'title': 'Média', 'value': 1 }, { 'title': 'Baixa', 'value': 0 }],
  'speed': [{ 'title': 'Alta', 'value': 2 }, { 'title': 'Média', 'value': 1 }, { 'title': 'Baixa', 'value': 0 }],

  'gender': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'is_tall': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'is_short': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'is_weight': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'is_light': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'is_bald': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],

  'eye_color': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'publisher': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }],
  'place_of_birth': [{ 'title': 'Sim', 'value': 1 }, { 'title': 'Não', 'value': 0 }] 
}

questionWithComplete = ['eye_color', 'publisher', 'place_of_birth']