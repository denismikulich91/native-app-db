<!-- markdownlint-disable MD001 MD024 -->
# Native App (CATIA) Database handler

### Tool containing three parts. 
### First part is a Native app hosted script used EKL bindings for Python. After every change of parameter in Parametric UG mine design, it pushes all parameters and other metadata into sqlite database.
### Second part is a RestAPI used Flask which responsible to fetch and post required data from the database.
### Third part is a 3DS platform hosted widget written using VUE.js framework, showing latest parameters of the tracking Mine design.

## Step 1. Update parameters of the parametric design
#### Python script runs automatically from EKL script, so user doesn't have to worry about updating database after every change.




https://github.com/denismikulich91/native-app-db/assets/105070976/0dda4c28-9a95-4437-b2ec-eed639eed8cd



## Step 2. Drop widget to the 3DS platform
#### After loading widget will automatically fetch the required data of the parametric mine.
##### NOTE: In case of several tracked UG mine designs sql database will have a few tables eacj dedicated to a specific parametric design. To fetch a specific table user just has to choose a table needed from the drop-down menu in the widget



https://github.com/denismikulich91/native-app-db/assets/105070976/4eff8339-430f-477a-8e18-7f3d81a8240d



## Commands for developers

| Command           | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| `npm run start`   | Build app continuously and serve @ `http://localhost:8081/widget` |
| `npm run startS3` | Build app continuously to `/dist/` and serve through AWS S3       |
| `npm run build`   | Build app to `/dist/`                                             |
| `npm run lint`    | Run ESLint                                                        |
| `npm run lintFix` | Run ESLint and fix issues                                         |
