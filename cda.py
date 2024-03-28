import numpy as np
# table elements
georgian_first_names = np.array(['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ',
                                 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ',
                                 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა',
                                 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი',
                                 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა',
                                 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა',
                                 'გოჩა', 'მურმან'])

georgian_last_names = np.array(
    ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი',
     'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე',
     'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია',
     'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე',
     'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა',
     'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე',
     'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია',
     'ქობალია', 'მიქავა', 'რევაზიშვილი'])

subjects = np.array(['მათემატიკა', 'ინგლისური', 'ალგორითები', 'CCNA შესავალი', 'Frontend'])

num_students = 100
num_subjects = len(subjects)

# generating table elements
random_first_names = np.random.choice(georgian_first_names, size=num_students)
random_last_names = np.random.choice(georgian_last_names, size=num_students)
random_full_names = np.array([f'{first} {last}' for first, last in zip(random_first_names, random_last_names)])
points = np.random.randint(0, 101, size=(num_students, num_subjects))

# Table design
table = np.column_stack((random_full_names, points))
table = np.vstack((np.concatenate((['სტუდენტი'], subjects)), table))
