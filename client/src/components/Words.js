import { useState, useEffect } from "react";
import React from "react";

import { Word } from "./Word";
import "../css/Words.css";

export const Words = () => {

  const [data, setData] = useState([{}]);

  useEffect(() => {
      fetch("/words").then(
      res => res.json()
      ).then(
      data => {
          setData(data)
      }
      )
  }, [])
  
  return (
    <table>
      <caption>Isogramic Words Found</caption>
      <thead>
        <tr>
          <th scope="col">Word</th>
          <th scope="col">Word Count</th>
          <th scope="col">Present in Files</th>
          <th scope="col">Sentences Containing Word</th>
        </tr>
      </thead>
      <tbody>
        {
        Object.entries(data).map(([word, wordInfo]) => {
          return (
            <Word 
              key={word}
              word={word}
              wordCount={wordInfo.word_count}
              filenames={wordInfo.file}
              sentences={wordInfo.sentence}
            />
          )
        })
        }
      </tbody>
    </table>
  )
};
