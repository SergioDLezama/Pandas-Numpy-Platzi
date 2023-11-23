import pandas as pd
import jumpline as jl
import numpy as np

df_books =pd.read_csv('./bestsellers-with-categories.csv')
print(df_books)
'''
                                                  Name                    Author  User Rating  Reviews  Price  Year        Genre
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7    17350      8  2016  Non Fiction
1                                    11/22/63: A Novel              Stephen King          4.6     2052     22  2011      Fiction
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7    18979     15  2018  Non Fiction
3                               1984 (Signet Classics)             George Orwell          4.7    21424      6  2017      Fiction
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     7665     12  2019  Non Fiction
..                                                 ...                       ...          ...      ...    ...   ...          ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9     9413      8  2019      Fiction
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2016  Non Fiction
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2017  Non Fiction
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2018  Non Fiction
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7    14331      8  2019  Non Fiction    

[550 rows x 7 columns]
'''

jl.run()

# Con el comando .head(numero) Podemos ver las primeras X numero de filas

df = df_books.head(3)
print(df)
'''
                                      Name              Author  User Rating  Reviews  Price  Year        Genre
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016  Non Fiction
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011      Fiction
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018  Non Fiction
'''

jl.run()

'''
Para eliminar las columnas solo para el output usamos .drop('nombre',axis=axis)
axis=0 Filas
axis=1 Columnas
'''

df = df_books.drop('Genre',axis=1).head(3)
print(df)
'''
                                      Name              Author  User Rating  Reviews  Price  Year
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018
'''

print('-'*15)

# Como podemos ver el DataFrame no se ha modificado, solo se borro genre para la salida de el codigo pasado
print(df_books.head(3))
'''
                                      Name              Author  User Rating  Reviews  Price  Year        Genre
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016  Non Fiction
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011      Fiction
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018  Non Fiction
'''

jl.run()

'''
Para eliminar definitivamente una fila o columna usamos inplace=True
df.drop('Nombre',axis=axis,inplace=True)
'''

df = df_books.drop('Genre',axis=1,inplace=True)
print(df) # None


print('-'*15)

# Como podemos ver el DataFrame se modifico
print(df_books.head(3))
'''
                                      Name              Author  User Rating  Reviews  Price  Year
0            10-Day Green Smoothie Cleanse            JJ Smith          4.7    17350      8  2016
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018
'''

jl.run()

'''
Otra forma es reescribiendo el data frame sin el inplace=
'''

df_books = df_books.drop('Reviews',axis=1)
print(df_books)
'''
                                                  Name                    Author  User Rating  Price  Year
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7      8  2016
1                                    11/22/63: A Novel              Stephen King          4.6     22  2011
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7     15  2018
3                               1984 (Signet Classics)             George Orwell          4.7      6  2017
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8     12  2019
..                                                 ...                       ...          ...    ...   ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9      8  2019
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7      8  2016
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7      8  2017
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7      8  2018
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7      8  2019
'''

jl.run()

'''
Tambien podemos eliminar columnas con del
'''

del df_books['Price']  
print(df_books)
'''
                                                  Name                    Author  User Rating  Year
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7  2016
1                                    11/22/63: A Novel              Stephen King          4.6  2011
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7  2018
3                               1984 (Signet Classics)             George Orwell          4.7  2017
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8  2019
..                                                 ...                       ...          ...   ...
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9  2019
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  2016
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  2017
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  2018
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  2019
'''

jl.run()

'''
Como eliminar filas
'''

# Recargamos el DataFrame
df_books =pd.read_csv('./bestsellers-with-categories.csv')

# Con drop eliminamos la fila 0
df = df_books.drop(0,axis=0).head(2)
print(df)
'''
                                      Name              Author  User Rating  Reviews  Price  Year        Genre
1                        11/22/63: A Novel        Stephen King          4.6     2052     22  2011      Fiction
2  12 Rules for Life: An Antidote to Chaos  Jordan B. Peterson          4.7    18979     15  2018  Non Fiction
'''

jl.run()

'''
Podemos borrar varias en una linea
'''

df = df_books.drop([0,1,2,3],axis=0).head(3)
print(df)

jl.run()

'''
Igualmente podemos borrar en rango
'''

df = df_books.drop(range(0,10),axis=0).head(2)
print(df)
'''
                                                 Name            Author  User Rating  Reviews  Price  Year        Genre
10                          A Man Called Ove: A Novel   Fredrik Backman          4.6    23848      8  2017      Fiction
11  A Patriot's History of the United States: From...  Larry Schweikart          4.6      460      2  2010  Non Fiction
'''

jl.run()

'''
Podemos agregar columnas con numpy
np.nan que significa quees un calor no numerico
'''

df_books['Nueva_Columna'] = np.nan
print(df_books.head(2))
'''
                            Name        Author  User Rating  Reviews  Price  Year        Genre  Nueva_Columna
0  10-Day Green Smoothie Cleanse      JJ Smith          4.7    17350      8  2016  Non Fiction            NaN
1              11/22/63: A Novel  Stephen King          4.6     2052     22  2011      Fiction            NaN
'''

jl.run()

'''
Podemos ver cuantas filas tenemos con .shape[0] y cuantas columnas  con .shape[1]
'''
print(df_books.shape[0]) # 550

print(df_books.shape[1]) # 8

jl.run()

# Creamos una array con todos las filas con np.arrange y shape

data = np.arange(0,df_books.shape[0])
print(data)
'''
[  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17
  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53
  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71
  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89
  90  91  92  93  94  95  96  97  98  99 100 101 102 103 104 105 106 107
 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125
 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143
 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161
 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179
 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197
 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215
 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233
 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251
 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269
 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287
 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305
 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323
 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341
 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359
 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377
 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395
 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413
 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431
 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449
 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467
 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485
 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503
 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521
 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539
 540 541 542 543 544 545 546 547 548 549]
'''

jl.run()

# Elimine la columna 'Genre'
del df_books['Genre']

# Agregamos una columna con cada numero asignado con el nombre rango

df_books['Rango'] = data
print(df_books)
'''
                                                  Name                    Author  User Rating  ...  Year  Nueva_Columna  Rango
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7  ...  2016            NaN      0      
1                                    11/22/63: A Novel              Stephen King          4.6  ...  2011            NaN      1      
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7  ...  2018            NaN      2      
3                               1984 (Signet Classics)             George Orwell          4.7  ...  2017            NaN      3      
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8  ...  2019            NaN      4      
..                                                 ...                       ...          ...  ...   ...            ...    ...      
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9  ...  2019            NaN    545      
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2016            NaN    546      
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2017            NaN    547      
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2018            NaN    548      
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2019            NaN    549 
'''

'''
Funciones para agregar filas
De forma rapida y sencilla .append()
.append() No me funciona a mi pero ._append() si
'''

jl.run()

df_books = df_books.append(df_books)
print(df_books)
'''
                                                  Name                    Author  User Rating  ...  Year  Nueva_Columna  Rango      
0                        10-Day Green Smoothie Cleanse                  JJ Smith          4.7  ...  2016            NaN      0      
1                                    11/22/63: A Novel              Stephen King          4.6  ...  2011            NaN      1      
2              12 Rules for Life: An Antidote to Chaos        Jordan B. Peterson          4.7  ...  2018            NaN      2      
3                               1984 (Signet Classics)             George Orwell          4.7  ...  2017            NaN      3      
4    5,000 Awesome Facts (About Everything!) (Natio...  National Geographic Kids          4.8  ...  2019            NaN      4      
..                                                 ...                       ...          ...  ...   ...            ...    ...      
545       Wrecking Ball (Diary of a Wimpy Kid Book 14)               Jeff Kinney          4.9  ...  2019            NaN    545      
546  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2016            NaN    546      
547  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2017            NaN    547      
548  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2018            NaN    548      
549  You Are a Badass: How to Stop Doubting Your Gr...               Jen Sincero          4.7  ...  2019            NaN    549      

[1100 rows x 8 columns]
'''
# A simple vista no hay mayor diferencia pero al final podemos ver que tenemos el doble de rows que antes

jl.run()

'''
Pandas .concat tambien es usado para agregar datos
'''

df_books = pd.concat([df_books,df_books])
print(df_books) # [2200 rows x 8 columns]
