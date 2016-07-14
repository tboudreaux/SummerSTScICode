from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[348.527417,23.563269],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_23116+2317/sdB_kuv_23116+2317_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_23116+2317/sdB_kuv_23116+2317_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
