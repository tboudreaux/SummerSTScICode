from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.900542,49.676792],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kpd_2237+4924/sdB_kpd_2237+4924_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kpd_2237+4924/sdB_kpd_2237+4924_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
