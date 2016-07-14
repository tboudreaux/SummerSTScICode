from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[89.009542,17.937103],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_0553+1755/sdB_kpd_0553+1755_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_0553+1755/sdB_kpd_0553+1755_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
