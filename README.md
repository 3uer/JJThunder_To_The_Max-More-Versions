# JJThunder To The Max (More Versions) 

This repository contains porting scripts to adapt **JJThunder** for Minecraft versions from **1.21.1** up to **1.21.11**.

---

##  Important Note for 1.21.11 Users
> [!TIP]
> If you are playing on Minecraft **1.21.11**, simply use the **1.21.9** version of the file. JJThunder will work perfectly fine without any extra patches.

---

##  Building Guide (Windows / Linux)

### Prerequisites
Before you begin, make sure you have Python installed on your system:
*  [Download Python](https://www.python.org/downloads/)

### Step-by-Step Instructions

1. **Prepare the workspace:** Create a folder containing your base archive `JJT.zip` along with all the Python scripts from this repository.
   
   <img width="695" alt="Folder Structure" src="https://github.com/user-attachments/assets/1c82a8c5-8b16-4997-8b2a-5b5c69e0d1a0" />

2. **Open the terminal:** Open `cmd` (Windows) or your terminal (Linux) inside that folder.
   
   <img width="477" alt="Opening CMD" src="https://github.com/user-attachments/assets/4db10e20-7d56-45b4-88d3-353a7f588eb4" />

3. **Run the conversion scripts:** Execute the scripts sequentially depending on your target version. Here is an example chain:

   
   # Step 1: Patch from 1.21.1 to 1.21.2
   `python 1_21_1_to_1_21_2.py JJT.zip`
   
   # Step 2: Patch the resulting file further (e.g., to 1.21.4)
   `python 1_21_3_to_1_21_4.py JJT_1_21_2.zip`
   
   # Step 3: Continue the chain to 1.21.7
   `python 1_21_6_to_1_21_7.py JJT_1_21_2.zip_1_21_4.zip`

Follow this logic to build any intermediate version you need!
 
### Contact & Support

If something went wrong, or you have any questions, feel free to reach out:

 Discord: 3uer
