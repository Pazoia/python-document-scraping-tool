import React from "react";

import "../css/Word.css";

export const Word = ({
  word,
  wordCount,
  filenames,
  sentences,
}) => {

  return (
    <tr>
      <th scope="row">{word}</th>
      <td>{wordCount}</td>
      <td>{filenames}</td>
      <td>{sentences}</td>
    </tr>
  ); 
};
