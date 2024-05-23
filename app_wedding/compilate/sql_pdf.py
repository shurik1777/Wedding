import pdfkit


def create_pdf(db):
    result_tuple = {
        'season': {'summer': 'Летом', 'autumn': 'Осенью', 'winter': 'Зимой', 'spring': 'Весной'}.get(db['season'],
                                                                                                     None),
        'amount': {'together': 'Только вдвоем', 'folks': 'Только близкие', 'morethan100': 'До 100',
                   'more100': 'Более 100'}.get(
            db['amount'], None),
        'place': {'restaurant': 'Банкетный зал', 'unique': 'Уникальная локация', 'garden': 'Вечеринка в саду',
                  'sea': 'Море'}.get(db['place'], None),
        'style': {'romantic': 'Романтическая свадьба', 'vintage': 'Винтажная свадьба',
                  'eccentric': 'Эксцентричная свадьба',
                  'modern': 'Современная свадьба', 'classic': 'Классическая свадьба',
                  'travel': 'Свадьба в стиле travel'}.get(db['style'], None),
        'colors': {'emeraldGreen': 'Изумрудно-зеленая', 'vanillaCream': 'Ванильная', 'macchiato': 'Капучино',
                   'dustyRose': 'Пыльная роза', 'wine': 'Винная', 'quartzPink': 'Розовый кварц'}.get(db['colors'],
                                                                                                     None),
        'fashion': {'trapezoidal': 'Трапециевидный силуэт', 'naiad': 'Русалка', 'sheath': 'Футляр',
                    'ballPown': 'Бальное платье', 'overalls': 'Комбинезон', 'retro': 'Ретро'}.get(db['fashion'],
                                                                                                  None),
        'costume': {'classicCostume': 'Классика', 'tuxedo': 'Смокинг', 'casual': 'Кэжуал',
                    'modernCostume': 'Современный костюм'}.get(db['costume'], None)
    }

    photo_season_path = {
        'summer': 'summer',
        'spring': 'spring',
        'autumn': 'autumn',
        'winter': 'winter'
    }.get(db['season'],
          'winter')

    photo_amount_path = {
        'two': 'two',
        'folks': 'folks',
        'upto100': 'upto100',
        'morethan100': 'morethan100'
    }.get(db['amount'], None)

    photo_place_path = {
        'restaurant': 'restaurant',
        'unique': 'unique',
        'garden': 'garden',
        'sea': 'sea'
    }.get(db['place'], None)

    photo_style_path = {
        'romantic': 'romantic',
        'vintage': 'vintage',
        'eccentric': 'eccentric',
        'modern': 'modern',
        'classic': 'classic',
        'travel': 'travel'
    }.get(db['style'], None)

    photo_colors_path = {
        'emeraldGreen': 'emeraldGreen',
        'vanillaCream': 'vanillaCream',
        'macchiato': 'macchiato',
        'dustyRose': 'dustyRose',
        'wine': 'wine',
        'quartzPink': 'quartzPink'
    }.get(db['colors'], None)

    photo_fashion_path = {
        'trapezoidal': 'trapezoidal',
        'naiad': 'naiad',
        'sheath': 'sheath',
        'ballGown': 'ballGown',
        'overalls': 'overalls',
        'retro': 'retro'
    }.get(db['fashion'], None)

    photo_costume_path = {
        'classicCostume': 'classicCostume',
        'tuxedo': 'tuxedo',
        'casual': 'casual',
        'modernCostume': 'modernCostume'
    }.get(db['costume'], None)

    with open('./app_wedding/compilate/index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    formatted_html = html_content.format(
        result_tuple['season'],
        photo_season_path,
        photo_season_path,
        photo_season_path,
        result_tuple['amount'],
        photo_amount_path,
        photo_amount_path,
        result_tuple['place'],
        photo_place_path,
        photo_place_path,
        photo_place_path,
        photo_place_path,
        result_tuple['style'],
        photo_style_path,
        photo_style_path,
        result_tuple['colors'],
        photo_colors_path,
        result_tuple['fashion'],
        photo_fashion_path,
        photo_fashion_path,
        photo_fashion_path,
        result_tuple['costume'],
        photo_costume_path,
        photo_costume_path,
        photo_costume_path
    )

    with open('./app_wedding/compilate/output.html', 'w', encoding='utf-8') as file:
        file.write(formatted_html)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

    pdfkit.from_file("./app_wedding/compilate/output.html", "./app_wedding/compilate/output.pdf",
                     verbose=True, options={"enable-local-file-access": True}, configuration=config)
