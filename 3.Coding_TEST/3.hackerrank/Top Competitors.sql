-- Top Competitors
-- #1.

select Hackers.hacker_id
     , Hackers.name
from Submissions
    inner join Hackers on Submissions.hacker_id = Hackers.hacker_id
    inner join Challenges on Submissions.challenge_id = Challenges.challenge_id
    inner join Difficulty on Difficulty.difficulty_level = Challenges.difficulty_level
where Difficulty.score = Submissions.score 
group by Hackers.hacker_id, Hackers.name
having count(distinct Submissions.submission_id) > 1
order by count(distinct Submissions.submission_id) desc, Hackers.hacker_id
