from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[345.641,26.049417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J230233.84+260257.9/sdB_LAMOST_J230233.84+260257.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J230233.84+260257.9/sdB_LAMOST_J230233.84+260257.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
