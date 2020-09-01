// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default (req, res) => {
  res.statusCode = 200
  res.json({
    stocks: ["첫번째종목", "두번째", "세번째", "네번째", "다섯번째"]
  })
}
