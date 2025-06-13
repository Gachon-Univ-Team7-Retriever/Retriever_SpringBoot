# 🛠️ 프로젝트 실행 가이드

## 📦 개발 환경
- **Java**: JDK 17
- **Framework**: Spring Boot
- **Build Tool**: Gradle (Wrapper)

## 🧰 사전 준비
1. **JDK 17**
   - 이 프로젝트는 JDK 17 버전으로 개발되었습니다.
   - IDE의 실행 버튼을 눌러 실행할 경우, **IDE에 설정된 JDK 버전**을 따릅니다.
     - **IntelliJ 기준**: `File > Project Structure > Project` 의 `SDK`에서 JDK 버전을 지정할 수 있습니다.
   - 터미널에서 명령어를 이용하여 실행할 경우, `build.gradle`에 설정된 **toolchain(JDK 17)** 버전이 자동으로 적용됩니다.

2. **IntelliJ IDEA (또는 다른 Java IDE)**
   - 프로젝트를 열면 `build.gradle` 파일을 인식하여 필요한 의존성을 자동으로 다운로드합니다.

3. **Database**
   - 이 프로젝트는 **MongoDB, Neo4j**를 사용합니다.
   - MongoDB 및 Neo4j 서버가 로컬 또는 지정된 주소에서 실행 중이어야 합니다.
   - `application.properties.example` 파일의 코드를 활용하여 `application.properties`에 DB 연결 정보를 설정해야 합니다.

## 🚀 실행 방법
### IDE에서 실행
- IDE에서 프로젝트를 열고 메인 클래스를 실행하거나, Gradle로 실행할 수 있습니다.

### Gradle 명령어로 실행
- 터미널에서 다음 명령어로 실행할 수 있습니다.
  ```
  ./gradlew bootRun
  ```
  - Windows의 경우
    ```
    gradlew bootRun
    ```
  - **permission denied: ./gradlew** 오류 발생 시, `gradlew` 파일에 실행 권한을 부여해야 합니다.
    ```
    chmod +x gradlew
    ```
