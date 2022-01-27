import { useState, useEffect } from "react";
import React from "react";

import { Word } from "./Word";

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
    <div className="word">
      <h1 className="title">Isogramic Words Found</h1>
      <div className="words">
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
      </div>
    </div>
  )
};
