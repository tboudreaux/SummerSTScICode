from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.481208,-56.032247],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lse_259/sdB_lse_259_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lse_259/sdB_lse_259_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
