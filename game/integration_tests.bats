@test "Show statements should specify an expression." {
    run grep -riI "show cat$"
    [ "${output}" = "" ]
}
