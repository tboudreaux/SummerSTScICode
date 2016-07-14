from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[61.522167,42.688953],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_0402+4232/sdB_kpd_0402+4232_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_0402+4232/sdB_kpd_0402+4232_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
