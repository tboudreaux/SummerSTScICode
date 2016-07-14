from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[80.130167,27.310475],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_05174+2716/sdB_KUV_05174+2716_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_05174+2716/sdB_KUV_05174+2716_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
