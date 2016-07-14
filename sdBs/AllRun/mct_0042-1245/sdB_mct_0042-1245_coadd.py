from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[11.238167,-12.481897],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_mct_0042-1245/sdB_mct_0042-1245_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_mct_0042-1245/sdB_mct_0042-1245_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
