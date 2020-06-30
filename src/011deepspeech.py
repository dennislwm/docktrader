#!/usr/bin/env python
# coding: utf-8

# # Mozilla DeepSpeech API Exploration
# 
# Mozilla released [DeepSpeech 0.6](https://github.com/mozilla/DeepSpeech/releases/tag/v0.6.0) with [APIs in C, Java, .NET, Python, and JavaScript](https://deepspeech.readthedocs.io/en/v0.6.0/Python-API.html).
# 
# From Colab menu, select: **Runtime** > **Change runtime type**, and verify that it is set to Python3, and select GPU if you want to try out GPU version.
# 
# You can install DeepSpeech with pip (make it deepspeech-gpu==0.6.0 if you are using GPU in colab runtime):
# 

# In[1]:


get_ipython().system('python --version')


# In[2]:


import os
import sys
get_ipython().system('{sys.executable} -m pip install deepspeech==0.6.0')


# ## Download Models and Audio Files
# 
# Mozilla has released models for US English, we will use those in this code lab.
# 
# 1. **Download the models:**
# 

# In[3]:


# Quick download go to URL: https://github.com/mozilla/DeepSpeech/releases
# !curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.0/deepspeech-0.6.0-models.tar.gz


# 2. **Unzip the downloaded models:**

# In[4]:


if not os.path.exists('deepspeech-0.6.0-models/'):
    get_ipython().system('tar -xvzf deepspeech-0.6.0-models.tar.gz')


# 3. **Download audio data files**

# In[5]:


# Quick download go to URL: https://github.com/mozilla/DeepSpeech/releases
# !curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.0/audio-0.6.0.tar.gz


# 4. **Unzip audio files**

# In[6]:


if not os.path.exists('audio/'):
    get_ipython().system('tar -xvzf audio-0.6.0.tar.gz')


# 5. **Test that it all works**

# In[7]:


get_ipython().system('deepspeech --model deepspeech-0.6.0-models/output_graph.pb --lm deepspeech-0.6.0-models/lm.binary --trie ./deepspeech-0.6.0-models/trie --audio ./audio/2830-3980-0043.wav')


# In[8]:


get_ipython().system('deepspeech --model deepspeech-0.6.0-models/output_graph.pb --lm deepspeech-0.6.0-models/lm.binary --trie ./deepspeech-0.6.0-models/trie --audio ./audio/4507-16021-0012.wav')


# In[9]:


get_ipython().system('deepspeech --model deepspeech-0.6.0-models/output_graph.pb --lm deepspeech-0.6.0-models/lm.binary --trie ./deepspeech-0.6.0-models/trie --audio ./audio/8455-210777-0068.wav')


# Examine the output of the last three commands, and you will see results *“experience proof less”*, *“why should one halt on the way”*, and *“your power is sufficient i said”* respectively. You are all set.

# # DeepSpeech API
# 
# 1.   **Import deepspeech**

# In[10]:


import deepspeech


# 2. **Create a model**

# In[11]:


model_file_path = 'deepspeech-0.6.0-models/output_graph.pbmm'
beam_width = 500
model = deepspeech.Model(model_file_path, beam_width)


# 3. **Add language model for better accuracy**

# In[12]:


lm_file_path = 'deepspeech-0.6.0-models/lm.binary'
trie_file_path = 'deepspeech-0.6.0-models/trie'
lm_alpha = 0.75
lm_beta = 1.85
model.enableDecoderWithLM(lm_file_path, trie_file_path, lm_alpha, lm_beta)


# ## Batch API
# 
# 1.   **Read an input wav file**
# 

# In[13]:


import wave
filename = 'audio/8455-210777-0068.wav'
w = wave.open(filename, 'r')
rate = w.getframerate()
frames = w.getnframes()
buffer = w.readframes(frames)


# Checkout sample rate and buffer type

# In[14]:


print(rate)
print(model.sampleRate())
print(str(type(buffer)))


# As you can see that the speech sample rate of the wav file is 16000hz, same as the model’s sample rate. But the buffer is a byte array, whereas DeepSpeech model expects 16-bit int array.
# 
# 2.  **Convert byte array buffer to int16 array**

# In[15]:


# skip this step if you are streaming the audio
import numpy as np
data16 = np.frombuffer(buffer, dtype=np.int16)
print(str(type(data16)))


# 3.  **Run speech-to-text in batch mode to get the text**

# In[16]:


# skip this step if you are streaming the audio
text = model.stt(data16)
print(text)


# ## Streaming API
# 
# Now let’s accomplish the same using streaming API. It consists of 3 steps: open session, feed data, close session.
# 
# 1.  **Open a streaming session**

# In[17]:


context = model.createStream()


# 2.  **Repeatedly feed chunks of speech buffer, and get interim results if desired**

# In[18]:


import numpy as np
buffer_len = len(buffer)
offset = 0
batch_size = 16384
text = ''
while offset < buffer_len:
    end_offset = offset + batch_size
    chunk = buffer[offset:end_offset]
    data16 = np.frombuffer(chunk, dtype=np.int16)
    model.feedAudioContent(context, data16)
    text = model.intermediateDecode(context)
    print(text)
    offset = end_offset


# 3.  **Close stream and get the final result**

# In[19]:


text = model.finishStream(context)
print(text)


# Verify that the output is same as as the batch API output: "your power is sufficient i said."

# # Recap
# 
# DeepSpeech has two modes: batch and streaming. First step is to create a model object, and then either call `stt()` or `feedAudioContnet()` to transcribe audio to text.
# <br/>
# 
# ---
# &copy; 2020 Satish Chandra Gupta
