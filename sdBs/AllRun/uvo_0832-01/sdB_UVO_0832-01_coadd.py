from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[128.849417,-1.931528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UVO_0832-01/sdB_UVO_0832-01_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UVO_0832-01/sdB_UVO_0832-01_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
