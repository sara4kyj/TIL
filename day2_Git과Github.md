## Git과 Github



#### Git 초기 설정

---

- 커밋기록 확인을 위한 이름과 이메일 설정

```bash
$ git config --global user.name "username"
$ git config --global user.email "aabbcc@abcdef.com"
```

- 설정 내역 확인

```bash
$ git config --global -l
or
$ git config --global -list
```





#### Git 기본 명령어

---

- 로컬 저장소 : 아래와 같은 과정으로 버전관리 수행

  - ```Working Directory ( = Working Tree)``` : 사용자의 작업공간

    ​			↓

  - ```Staging Area ( = Index)``` : 커밋을 위한 파일 및 폴더가 추가되는 곳

    ​			↓

  - ```Repository : staging area```에 있던 파일 및 폴더의 변경사항(커밋)을 저장



- ```git init``` : 현재 작업중인 디렉토리를 Git으로 관리하겠다는 명령어

  - ```.git``` 숨김 폴더 생성 / 터미널에는 ```(master)``` 표기
  - Mac OS의 경우 ```(master)```를 표기하고 싶다면 Terminal 업그레이드를 진행

  ```tex
  ※ 주의 사항
     	- git init는 중첩 금지
     	- 경로 확인 필수	
  ```



- ```git status``` : Working Directory와 Staging Area에 있는 파일의 상태를 알려주는 명령어

  - 수시로 status를 확인하면 좋음

  - 상태

    1. Untracked : Git이 관리하지 않는 파일
    2. Tracked : Git이 관리하는 파일
       - Unmodified : 최신 상태
       - Modified : 수정되었지만 Staging Area에 반영하지 않은 상태
       - Staged : Staging Area에 올라간 상태

    

- ```git add``` : Working Dierctory에 있는 파일을 Staging Area로 올리는 명령어

  - Git이 해당 파일을 추적(관리)할 수 있도록 만들어줌
  - ```Untracked, Modified -> Staged``` 로 상태 변경

  

- ```git commit``` : Staging Area에 올라온 파일의 변경사항을 하나의 버전(커밋)으로 저장

  - `commit message`는 변경사항을 잘 나타낼 수 있도록 작성
  - 각 커밋은 `SHA-1`알고리즘에 의해 반환된 고유의 해시값을 ID로 가짐
  - `(root-commit)`은 최초 커밋일 때만 표시
  - `vim`진입시 `[esc] :wq [enter]`

  

- `git log` : 커밋의 내역 조회

  - `--oneline` : 한 줄로 축약해 출력
  - `--graph` : 브랜치와 머지 내역을 그래프로 출력
  - `-all` : 모든 브랜치 내역 출력
  - `--reverse` :  커밋 내역의 순서를 반대로 출력(최신이 가장 아래)
  - `-p` : 파일의 변경내용도 같이 출력
  - `-2` : 원하는 개수 만큼의 내역 출력	





