#1. 최대값 구하기

SELECT MAX(DATETIME)
FROM ANIMAL_INS


#2. 최솟값 구하기

SELECT MIN(DATETIME)
FROM ANIMAL_INS


#3. 동물 수 구하기

SELECT COUNT(DISTINCT ANIMAL_ID)
FROM ANIMAL_INS


#4. 중복 제거하기

SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
