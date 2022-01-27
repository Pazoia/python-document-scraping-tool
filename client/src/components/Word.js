import React from "react";

export const Word = ({
  word,
  wordCount,
  filenames,
  sentences,
}) => {

  return (
    <div className="word">
      <ul key={word}>
        <li>{word}</li>
        <li>{wordCount}</li>
        <li>{filenames}</li>
        <li>{sentences}</li>
      </ul>
    </div>
  ); 
};
