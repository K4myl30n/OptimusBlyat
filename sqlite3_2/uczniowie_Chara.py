
�Y�  �               @   s�   d  d l  Z  d d �  Z d d �  Z d d �  Z d d	 �  Z d
 d �  Z d d �  Z d d �  Z d d �  Z d d �  Z	 d d �  Z
 d d �  Z e d k r� d  d l Z e j e e j � � d S)�    Nc             C   s1   |  j  �  } x | D] } t t | � � q Wd  S)N)Zfetchall�print�tuple)�cur�wyniki�row� r   �uczniowie_Teter.pyr      s    r   c             C   s   |  j  d � d  S)Nz�
        SELECT Imie, Nazwisko, tbKlasy.klasa
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.klasaID=tbKlasy.IDklasy
        AND tbKlasy.Klasa = '1A'
        )�execute)r   r   r   r   �kw_a   s    r
   c             C   s   |  j  d � d  S)Nz=
        SELECT MAX(EgzHum)
        FROM tbUczniowie
        )r	   )r   r   r   r   �kw_b   s    r   c             C   s   |  j  d � d  S)Nz�
        SELECT AVG(EgzMat)
        FROM tbUczniowie, tbKlasy
        WHERE tbUczniowie.klasaID=tbKlasy.IDklasy
        AND tbKlasy.Klasa = '1A'
        )r	   )r   r   r   r   �kw_c   s    r   c             C   s   |  j  d � d  S)Nz�
        SELECT Imie, Nazwisko, tbOceny.Ocena
        FROM tbUczniowie, tbOceny
        WHERE tbOceny.UczenID = tbUczniowie.IDucznia
        AND Imie = "Dorota" 
        AND Nazwisko = "Nowak"
        )r	   )r   r   r   r   �kw_d(   s    r   c             C   s   |  j  d � d  S)Nz�
        SELECT AVG(Ocena)
        FROM tbOceny, tbPrzedmioty
        WHERE strftime('%m', datad) LIKE '10'
        AND tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
        AND tbPrzedmioty.Przedmiot = 'fizyka'
       )r	   )r   r   r   r   �kw_e2   s    r   c             C   s    |  j  d d  d d d g � d  S)Nz:
        INSERT INTO tbKlasy
        VALUES (?,?,?,?)
    Z3Ci�  i�  )r	   )r   r   r   r   �dodaj;   s    r   c             C   s   |  j  d d d g � d  S)NzL
        UPDATE tbKlasy
        SET klasa = ?
        WHERE IDKlasy = ?
    Z3D�   )r	   )r   r   r   r   �
aktualizujA   s    r   c             C   s    |  j  d d d d d g � d  S)Nzl
    UPDATE tbUczniowie
    SET EgzJez = ?
    WHERE Imie = ?
    AND Nazwisko = ?
    AND IDucznia = ?
    �#   ZPaulinaZDziedzic�   )r	   )r   r   r   r   �aktH   s    r   c             C   s   |  j  d d d g � d  S)Nz5DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?Z3Bi�  )r	   )r   r   r   r   �usunR   s    r   c             C   sR   t  j d � } | j �  } t  j | _ t | � | j �  t | j d � � d S)Nz	szkola.dbzSELECT * FROM tbUczniowier   )	�sqlite3ZconnectZcursorZRowZrow_factoryr   Zcommitr   r	   )�argsZconr   r   r   r   �mainV   s    

r   �__main__)r   r   r
   r   r   r   r   r   r   r   r   r   �__name__�sys�exit�argvr   r   r   r   �<module>   s   		
	
