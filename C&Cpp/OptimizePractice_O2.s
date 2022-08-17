	.file	"OptimizePractice.c"
	.text
	.p2align 4,,15
	.globl	_operate
	.def	_operate;	.scl	2;	.type	32;	.endef
_operate:
LFB12:
	.cfi_startproc
	testb	$1, 4(%esp)
	movl	8(%esp), %eax
	je	L1
	addl	$1, (%eax)
L1:
	rep ret
	.cfi_endproc
LFE12:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "%d\12\0"
	.section	.text.startup,"x"
	.p2align 4,,15
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	xorl	%eax, %eax
	xorl	%edx, %edx
	jmp	L8
	.p2align 4,,10
L10:
	movl	%eax, %ecx
	andl	$1, %ecx
	cmpl	$1, %ecx
	sbbl	$-1, %edx
L8:
	addl	$1, %eax
	cmpl	$10, %eax
	jne	L10
	movl	%edx, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	xorl	%eax, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
