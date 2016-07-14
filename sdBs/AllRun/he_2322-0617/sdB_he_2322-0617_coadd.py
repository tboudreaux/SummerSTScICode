from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[351.382917,-6.020028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_2322-0617/sdB_he_2322-0617_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_2322-0617/sdB_he_2322-0617_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
