
���Y  �               @   s�   d  d l  Z  d d �  Z d d �  Z d d �  Z d d	 �  Z d
 d �  Z d d �  Z e d k r� d  d l Z e j	 e e j
 � � d S)�    Nc             C   s>   |  j  d � |  j �  } x | D] } t t | � � q  Wd  S)Nz�
        SELECT Imie, Nazwisko, tbKlasy.klasa
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.klasaID=tbKlasy.IDklasy
        AND tbKlasy.Klasa = '1A'
        )�execute�fetchall�print�tuple)�cur�wyniki�row� r	   �uczniowie.py�kw_a	   s
    r   c             C   sG   |  j  d t t f � |  j �  } x | D] } t t | � � q) Wd  S)Nz^
        SELECT Imie, Nazwisko, EgzHum
        FROM tbUczniowie
        WHERE  EgzHum
        )r   ZnazwaZsiedzr   r   r   )r   r   r   r	   r	   r
   �kw_b   s
    r   c             C   s>   |  j  d � |  j �  } x | D] } t t | � � q  Wd  S)Nz�
        SELECT nazwisko, stanowisko, pracownicy.placa *
        
        (SELECT premia.premia 
        FROM premia
        WHERE pracownicy.stanowisko = premia.id)
        AS premia
        FROM pracownicy
        ORDER BY premia DESC
        )r   r   r   r   )r   r   r   r	   r	   r
   �kw_c    s
    	r   c             C   s|   |  j  d � } | j �  } x | D] } t t | � � q" W|  j  d � } | j �  } x | D] } t t | � � q^ Wd  S)NzX
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie LIKE '%a'
        z\
        SELECT AVG(placa)
        FROM pracownicy
        WHERE imie NOT LIKE '%a'
        )r   r   r   r   )r   Zkobietyr   r   Zmenr	   r	   r
   �kw_d0   s    		r   c             C   s>   |  j  d � |  j �  } x | D] } t t | � � q  Wd  S)NzP
        SELECT imie, nazwisko,stanowisko (JulianDay())
        
       
       )r   r   r   r   )r   r   r   r	   r	   r
   �kw_eE   s
    r   c             C   s5   t  j d � } | j �  } t  j | _ t | � d S)Nz	szkola.dbr   )�sqlite3ZconnectZcursorZRowZrow_factoryr   )�argsZconr   r	   r	   r
   �mainR   s
    
r   �__main__)r   r   r   r   r   r   r   �__name__�sys�exit�argvr	   r	   r	   r
   �<module>   s   	