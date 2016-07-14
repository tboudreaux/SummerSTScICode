from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[264.360333,22.149356],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UVO_1735+22/sdB_UVO_1735+22_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UVO_1735+22/sdB_UVO_1735+22_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
