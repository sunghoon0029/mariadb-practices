package com.bitacademy.emaillist.main;

import java.util.List;
import java.util.Scanner;

import com.bitacademy.emaillist.dao.EmaillistDao;
import com.bitacademy.emaillist.vo.EmaillistVo;

public class EmaillistApp {
	private static Scanner scanner = null;
	
	public static void main(String[] args) {
		scanner = new Scanner(System.in);
		
		while (true) {
			System.out.print("(l)ist, (a)dd, (d)elete, (q)uit > ");
			String commend = scanner.nextLine();

			if ("l".equals(commend)) {
				doList();
			} else if ("a".equals(commend)) {
				doAdd();
			} else if ("d".equals(commend)) {
				doDelete();
			} else if ("q".equals(commend)) {
				break;
			}
		}
		
		scanner.close();
	}

	private static void doDelete() {
		System.out.println("이메일:");
		String email = scanner.nextLine();
		
		new EmaillistDao().deleteByEmail(email);
		
		doList();
	}

	private static void doAdd() {
		System.out.print("성:");
		String firstName = scanner.nextLine();
		
		System.out.print("이름:");
		String lastName = scanner.nextLine();
		
		System.out.print("이메일:");
		String email = scanner.nextLine();
		
		EmaillistVo vo = new EmaillistVo();
		vo.setFirstName(firstName);
		vo.setLastName(lastName);
		vo.setEmail(email);
		
		new EmaillistDao().insert(vo);
		
		doList();
		
	}

	private static void doList() {
		List<EmaillistVo> list = new EmaillistDao().findAll();
		for(EmaillistVo vo : list) {
			System.out.println("이름:" + vo.getFirstName() + " " +  vo.getLastName() + "이메일:" + vo.getEmail());
		}
	}
}
