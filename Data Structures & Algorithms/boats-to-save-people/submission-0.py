class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        """
        people: integer array, each element corresponds ot the weight of that person
        infinite # of boats, each boat can carry a max weight of limit
        at most 2 people, but must be <= limit
        each person <= limit
        each person >=1
        hashset



        [1,3,2,3,2] limit = 3
        [1,2,2,3,3]

        """
   

        boats = 1
        people = sorted(people)
        
        r = len(people) -1
        l = 0
        boats = 0

        while l <= r:
            if people[l] + people[r] > limit:
                boats +=1
                r-=1
            elif people[l] + people[r] <= limit:
                boats +=1
                l+=1
                r-=1
        
        return boats
                
