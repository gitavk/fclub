2015/04/13
Списание товаров.

2015/04/09
Изменен алгоритм активации договоров

2015/01/18
Отчет по продажам менеджеров за период.

2015/01/18
Отчет об окончании контракта.
Кнопка погашния для иное.

2014/11/06
Исправленна ошибка блокировки перспективного договора.
Дообавлена функция вывода первого визита по договору.

2014/10/26
Добавлена логика отмены продажы в базе.

2014/10/25
Менеджер при продлении.

2014/10/22
Отчет должники по менеджеру.

2014/10/08
Добавлена индикация ожидания ответа от сервера

2014/09/26
Удаление кавычек из наименования товара для кассы.

2014/09/25
Расширенный отчет находящихся в клубе.

2014/09/23
Асинхронная печать отчетов по кассе.(Для ожидания предыдущего ответа)

2014/09/23
Изменение персональных данных клиента.
Скрытие иконок главного меню для ресепшен.

2014/09/22
Изменение номера карты по договору

2014/09/21
Обновление фото клиента.
Contract.objects.all().update(is_current=2)

2014/09/19
Заменить отчет рецепциониста на "чеки по кассе",
отчет рецепциониста перенесен в отчеты в формате Excel.

2014/09/14
Отчет список сотрудников
Отчет статистика по сотруднику

2014/09/03
Добавлено слово 'без скидки' при скидки равно 0.
При переоформлении добавлена галочка смена плательщика.

2014/08/31
Скрытие требования визита при выборе клиента
добавление имени в списке выбора клиентов при оплате
При редактировании услуги (в справочнике) - выдает ошибку;
Сделать список услуг по алфавиту;
Выводить в списке услуг СТОИМОСТЬ услуги (напротив наименования услуги, также как и в договорах)
история платежей - если без имени

2014/08/27
Удаление внутренней накладной

2014/08/20
отчет по отделам разнес с отчетом гашения на стороне кассы
подготовка к откату чека
при продлении договора необходимо, чтобы вылазила следующая информация(есть ли действующий договор и какой, его цена и скидка, с которой он покупался.
Необязателен штрих-код в услугах (разовые)
При создании ПТТ - присвоение должности.
Абонемент 6 месяцев = 182 дня
Добавить кнопки "Удалить" в список со скидками.

2014/08/19
удалять долг с клиента;

2014/08/17
Копейки в итоговой сумме после запятой показывают аж до миллиардных сотых)
Нужно, чтобы только 2 знака после запятой в итоговой сумме было.
После добавления еще позиций в приходную накладную - 
итоговая сумма перестала считаться...

2014/08/15
Редактирование внутренней накладной

2014/08/09
Продажа без клиента

2014/08/08
Исправлен ряд замечений

2014/08/07
отчет менеджера

2014/08/06
изменить отчеты: посещения клуба оба
График дежурств в тренажерном зале

2014/08/03
список дожностее ПТТ индивидуален для каждого блока ПТТ
смена должность с фильтром по департаменту

2014/08/02
Сделать поставщиков по алфавиту
По алфавиту виды товаров
По алфавиту ассортимент товаров
иероглифы в приходной накладной
Выдает ошибку при вводе копеек в себестоимости продукта
Длинное название вида товаров
"Годен до" в Приходной накладной
Выровнять Поставщиков в Справочнике
Добавить в экселевский файл месячного отчета:
1) название месяца и год, за который выводится отчет;
2) справа вверху надпись "генеральный...", как в образце;
3) сделать так, чтобы неиспользуемые отделы не выводились в отчет;
4) над названиями отделов добавить строку с самими отделами;
список дожностее ПТТ индивидуален для каждого блока ПТТ

2014/08/01
Заметка по сотруднику
Отчет по персональным тренировкам
Выдача карт по персональным тренировкам

2014/07/31
Отчет: Посещения клуба за период
Сотрудники вход в клуб
Отчет: Посещения клуба сотрудниками

2014/07/30
Тип товара или услуги только для клиентов.

2014/07/30
Отчет: продажи за месяц

2014/07/29
Переоформление:
поиск только неактивных клиентов(без договоров) клиентов или внесение нового

Пролонгация исправлять менеджера если это гость

2014/07/28
Удаление 'Входящей накладной'
Названия отделов

2014/07/27
Переоформление договора
смена должности для сотрудника
увольнение сотрудника

2014/07/26
Бонус к договору
Расторжение договора
Заметка по клиенту

2014/07/25
Клиенты из металинка
Разовый визит

2014/07/23
Цена товара на дату.
Номер отдела платежа.
Отчет рецепчиониста.

2014/07/22
Пролонгация для гостей и клиентов.
Тип платежа в историю.

2014/07/21
Добавлен справочник и продажа блоков персональных тренировок.

2014/07/12
Добавлено редактирование входящей накладной с проверкой.
Изменено отображение цены в товаре по умолчанию указываеться дата текущей цены.
Редактирование персонала.

2014/07/12
Исправленна ошибки:
 - при редактировании гостя, теперь можно только своего.
 - отображение цены по умолчанию, с копейками
 - шаг цены сделан в 1 копейку
Добавлена опция для суперпользователя - право менять менеджера у клиента.

2014/07/07
Добавлен font-awesome-4.1.0
Добавлены кнопки на форму печати договора
В карточке клиента по умолчанию для менеджера открываються долги по абонименту
Изменена иконка о наличии сообщений

2014/07/06
Настройка для удаленной работы с кассой.
Инструменты начальной загрузки договоров в базу.

2014/07/02
Добавлено:
Интерфейс работы с кассой
Модели для работы с сотрудниками

2014/06/30
Добавлено:
Внутреннее перемещение в торговую точку.
Повесить долг на клиента гостя.
Касса печать чеков.
Инструмент для загрузки клиентов из csv.

2014/06/20
Добавлено:
Ресепшен карта гостя, платежи(без чека)

2014/06/14
Добавлено:
Ресепшен меню, напоминания, отчет о днях рождения

2014/06/10
Добавлено:
- данные о всех контрактах в карту клиента.
- модуль товараооборот до прихода товара включительно.
Исправлено:
- постоянный атоответ при чтении уведомлений

2014/06/06
Сохранение входящих накладных.
Поиск заменен на contains.
Сохранение платежей при редактировании схемы платежей в договоре.

Добавлен органайзер:
- регистрация гостя
- напоминаня
Изменен User по умолчанию
Изменены форма и свойства товара
Добавлена форма входящей накладной на склад
Сохранение накладной.
Скрип авто активации и закрытия договоров.
Закрытие повизитовых договоров после последнего входа.
Схема кредитов изменена. История выделена в отдельную таблицу.