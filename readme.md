This is the start of a blog post I will work on for realpython.com

So sometimes problems just hit you and you know you just HAVE to solve them. The Kaggle competition Santa’s Little Helpers was just one of those for me. Around the time I read it about the competition RealPython.com graciously offered to let me do a guest blog post and I thought this would be a great fit.

I immediately started to try to optimize a solution in my head (not with code..), but remembered Donald Knuth’s wise words “Premature optimization is the root of all evil”.

So the competition is here: http://www.kaggle.com/c/helping-santas-helpers

I won’t go into the detail about the problem description here, but advise you to read through it. I read it 3-4 times initially to understand the problem and will probably read it 20 more times by the end of the week. Just get comfortable with the problem or reference it as you follow along.

So my first step is to just get a working solution. I want to be able to write some code to be able to work with the problem so that I can actually submit something and get on the leaderboard. This will motivate me to iterate to find an optimized solution (and it is rewarding to climb the competition ladder).

I want to figure out how I would solve this if I was Santa and had to actually make the decisions in real life before I write any code. I know that I have incoming toy orders and they take a certain amount of time to make. I need a way to track incoming orders and the amount of time that it will take to make them. I know that I have a fixed labor pool and when a laborer starts working on a toy they have to finish. I want to be able to watch for incoming toy orders and assign a laborer to work on the toy. If I get more orders than laborers then I need to queue my incoming orders. Laborers have sanctioned and unsanctioned work hours. I need to keep track of the hours they work for two reasons. If they work unsanctioned hours then they get an equivalent amount of rest when they are done with their toy. These hours affect their productivity. I need a way to track the availability of workers. I need a way to track the productivity of a worker before and after a toy.

Things to keep track of:
- Toy Orders
- Amount of time to complete an order
- Queue for orders to be filled
- Completed Orders
- Individual Laborers
- A laborers sanctioned hours worked
- A laborers unsanctioned hours worked
- Available workers
- Productivity of a worker before a toy
- Productivity of a worker after a toy

After writing out a description of things I will need to track as Santa I can write them out a little further as ‘variables’ which I will show throughout my code with comments. Now I need some actions Santa can do in order to manage his workshop.

When he receives a new order he wants to first check to see if he has an available worker in the labor pool. If he does then he wants to assign that worker to the toy. He wants to apply the workers productivity metric against how much time it will take to complete the toy, this is done by dividing time to complete the toy by the productivity metric. This lets Santa know when he will be done. Further Santa needs to know when he starts and when he stops to determine if he is working during sanctioned hours or unsanctioned hours. After the worker completes the toy then Santa needs to mark down his new productivity based on the amount of time the worker contributed to a toy against the sanctioned or unsanctioned hours. Then Santa can release the worker to go back into the labor pool and check off that the toy has been completed.

Actions:
- Check order queue
- Check labor pool
- Assign worker from labor pool
- Measure time to complete toy with productivity metric and time to complete toy
- Sanctioned or unsanctioned tracker during toy production
- New productivity issuer
- Release worker from labor pool
- Toy completed checker