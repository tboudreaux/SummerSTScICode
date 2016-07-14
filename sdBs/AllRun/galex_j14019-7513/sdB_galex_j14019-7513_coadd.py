from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[210.480542,-75.225875],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j14019-7513/sdB_galex_j14019-7513_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j14019-7513/sdB_galex_j14019-7513_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
