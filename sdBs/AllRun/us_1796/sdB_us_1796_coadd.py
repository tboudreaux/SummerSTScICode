from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[132.874542,43.918742],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_us_1796/sdB_us_1796_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_us_1796/sdB_us_1796_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
