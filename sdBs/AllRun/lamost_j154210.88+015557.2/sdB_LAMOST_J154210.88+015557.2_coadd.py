from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[235.545333,1.932556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J154210.88+015557.2/sdB_LAMOST_J154210.88+015557.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J154210.88+015557.2/sdB_LAMOST_J154210.88+015557.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
