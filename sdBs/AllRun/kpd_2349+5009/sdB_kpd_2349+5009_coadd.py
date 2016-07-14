from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[358.031417,50.446133],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_2349+5009/sdB_kpd_2349+5009_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_2349+5009/sdB_kpd_2349+5009_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
