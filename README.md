# ChatGPT Command Tool

## Environment

Create `.env` file with the following content:
 ```dotenv
OPEN_AI_URL="https://api.openai.com/v1"
OPEN_AI_API_KEY=<YOUR_API_KEY>
 ```

## Arguments

**-o --operation (default=txt)**

Indicates the operation to execute.\
Possible values are: `img | txt`

**-s --size (only for img)**

Indicates the size of the generated image.\
Possible values are: `1024 | 512 | 256`

**-c --continuous (only for txt)**

This field indicates if the tool should keep asking for new prompts after ChatGPT response.

**-p --prompt**

This field sets the initial prompt to request ChatGPT.

## Examples

### Text Geneartion

 ```sh
python3 src/main.py -p "Hi"
 ```

![img.png](public/txt_result.png)

### Image Geneartion
3. Enter your prompt:  
 ```sh
python3 src/main.py -oimg -s1024 -p "ocean painting"
 ```

4. Enjoy the result:  
![result.png](public%2Fimg_result.png)