# Ethical Threshhold benchmark from Andon Hackathon

This is the code from the group that measured at what point an LLM would go from helping the starving user by stealing from a poor person to refusing to steal from the poor person. The point was to find a prompt which would simulate an AGI or very intelligent AI helping the creator or user of it make money on the expense of others, which is a likely scenario, for instance if the stock market was chosen as an arena. The prompt was quite hard to find, therefore it might seem slightly off-mark from the goal.

![AI Moral Decision Graph](moral_threshold_plot_10_trials.png)

Run the code by setting up a python environment, entering your OpenAI API key in chat2.py, and then running the chat2.py and plot_results.py files.

```bash
python -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Enter your OpenAI API key in chat2.py.

```bash
python chat2.py
```

```bash
python plot_results.py
```
